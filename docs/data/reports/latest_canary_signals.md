# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T20:11:11.869138+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0363` n `12`; crypto_alt avg `-0.0861` n `230`; crypto_major avg `-0.0654` n `8`; equity avg `-0.0938` n `114`; fx avg `0.0028` n `6`; index avg `0.0005` n `25`; metal avg `0.0064` n `20`; unknown avg `0.0295` n `792`
- 1h: commodity avg `0.0826` n `12`; crypto_alt avg `-0.1388` n `230`; crypto_major avg `-0.0791` n `8`; equity avg `-0.0957` n `114`; fx avg `-0.0106` n `6`; index avg `-0.0059` n `25`; metal avg `0.0541` n `20`; unknown avg `0.1268` n `792`
- 4h: commodity avg `0.4246` n `12`; crypto_alt avg `-0.2852` n `230`; crypto_major avg `-0.217` n `8`; equity avg `-0.614` n `114`; fx avg `0.0067` n `6`; index avg `-0.1408` n `25`; metal avg `-0.1114` n `20`; unknown avg `0.1267` n `792`
- 24h: commodity avg `0.3949` n `12`; crypto_alt avg `-0.264` n `230`; crypto_major avg `0.6945` n `8`; equity avg `0.9931` n `114`; fx avg `0.0114` n `6`; index avg `0.0585` n `25`; metal avg `0.1949` n `20`; unknown avg `0.241` n `775`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1846`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1713`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1396`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.122`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0978`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0973`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0961`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0949`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0922`, n `668`, weak_sample_signal
