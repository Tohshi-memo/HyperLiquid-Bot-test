# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-15T10:44:18.963204+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0131` n `12`; crypto_alt avg `-0.0286` n `230`; crypto_major avg `-0.0446` n `8`; equity avg `-0.0104` n `114`; fx avg `0.0006` n `6`; index avg `-0.0003` n `25`; metal avg `0.0006` n `20`; unknown avg `-0.0803` n `791`
- 1h: commodity avg `-0.0346` n `12`; crypto_alt avg `0.0618` n `230`; crypto_major avg `-0.0206` n `8`; equity avg `0.0085` n `114`; fx avg `-0.008` n `6`; index avg `-0.0049` n `25`; metal avg `-0.009` n `20`; unknown avg `-0.0193` n `791`
- 4h: commodity avg `-0.1152` n `12`; crypto_alt avg `0.0657` n `230`; crypto_major avg `-0.1576` n `8`; equity avg `0.0524` n `114`; fx avg `-0.0103` n `6`; index avg `0.0026` n `25`; metal avg `0.0124` n `20`; unknown avg `-0.0098` n `791`
- 24h: commodity avg `-0.0543` n `12`; crypto_alt avg `1.0757` n `230`; crypto_major avg `0.0579` n `8`; equity avg `-0.4998` n `114`; fx avg `0.1254` n `6`; index avg `-0.1357` n `25`; metal avg `0.2328` n `20`; unknown avg `-0.139` n `754`

## Correlations

- news_risk_score -> equity_forward_1h_return_pct: corr `0.2156`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1904`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1825`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1743`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1538`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1496`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1458`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.141`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1385`, n `668`, weak_sample_signal
