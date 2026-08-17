# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-17T20:48:28.026955+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0115` n `12`; crypto_alt avg `0.0764` n `230`; crypto_major avg `0.0357` n `8`; equity avg `-0.0077` n `114`; fx avg `-0.0039` n `6`; index avg `-0.0127` n `25`; metal avg `0.0003` n `20`; unknown avg `-0.021` n `792`
- 1h: commodity avg `0.0707` n `12`; crypto_alt avg `0.0829` n `230`; crypto_major avg `0.0805` n `8`; equity avg `-0.1037` n `114`; fx avg `0.0093` n `6`; index avg `-0.0234` n `25`; metal avg `-0.0135` n `20`; unknown avg `-0.0796` n `792`
- 4h: commodity avg `0.406` n `12`; crypto_alt avg `-0.0636` n `230`; crypto_major avg `-0.0959` n `8`; equity avg `-0.6382` n `114`; fx avg `0.0067` n `6`; index avg `-0.1372` n `25`; metal avg `-0.0835` n `20`; unknown avg `-0.0084` n `792`
- 24h: commodity avg `0.4078` n `12`; crypto_alt avg `0.1509` n `230`; crypto_major avg `0.9975` n `8`; equity avg `0.9847` n `114`; fx avg `0.0182` n `6`; index avg `0.0415` n `25`; metal avg `0.2057` n `20`; unknown avg `0.2189` n `775`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1856`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1722`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1511`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1401`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1223`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.103`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0969`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0948`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0928`, n `668`, weak_sample_signal
