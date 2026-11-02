# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-02T00:37:25.699310+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0275` n `13`; crypto_alt avg `0.0518` n `238`; crypto_major avg `0.1439` n `8`; equity avg `0.2055` n `156`; fx avg `0.0328` n `6`; index avg `0.0583` n `27`; metal avg `-0.0272` n `20`; unknown avg `-0.1332` n `1261`
- 1h: commodity avg `0.0717` n `13`; crypto_alt avg `-0.4983` n `238`; crypto_major avg `-0.158` n `8`; equity avg `0.2731` n `156`; fx avg `0.0729` n `6`; index avg `0.1491` n `27`; metal avg `-0.0132` n `20`; unknown avg `0.8031` n `1249`
- 4h: commodity avg `0.0562` n `13`; crypto_alt avg `-0.2097` n `238`; crypto_major avg `0.1164` n `8`; equity avg `0.4161` n `156`; fx avg `0.0947` n `6`; index avg `0.1502` n `27`; metal avg `0.0869` n `20`; unknown avg `0.8029` n `1219`
- 24h: commodity avg `-0.029` n `13`; crypto_alt avg `-0.8865` n `238`; crypto_major avg `-0.2203` n `8`; equity avg `0.6615` n `156`; fx avg `0.087` n `6`; index avg `0.2216` n `27`; metal avg `0.1157` n `20`; unknown avg `3.6155` n `1130`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `0.16`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1589`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1568`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1553`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1293`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1273`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1199`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.0966`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0922`, n `668`, weak_sample_signal
