# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-17T15:07:26.648048+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0194` n `13`; crypto_alt avg `-0.3179` n `236`; crypto_major avg `-0.1573` n `8`; equity avg `-0.0411` n `151`; fx avg `-0.0013` n `6`; index avg `0.0041` n `26`; metal avg `-0.0031` n `20`; unknown avg `0.0375` n `1183`
- 1h: commodity avg `-0.1294` n `13`; crypto_alt avg `0.0327` n `236`; crypto_major avg `0.1224` n `8`; equity avg `-0.0271` n `151`; fx avg `-0.0043` n `6`; index avg `0.005` n `26`; metal avg `-0.0108` n `20`; unknown avg `0.52` n `1173`
- 4h: commodity avg `0.0481` n `13`; crypto_alt avg `-1.0585` n `236`; crypto_major avg `-0.4751` n `8`; equity avg `-0.2352` n `151`; fx avg `-0.013` n `6`; index avg `-0.0369` n `26`; metal avg `-0.0263` n `20`; unknown avg `3.1325` n `1167`
- 24h: commodity avg `0.7735` n `13`; crypto_alt avg `-2.0201` n `236`; crypto_major avg `-0.6199` n `8`; equity avg `-1.6099` n `151`; fx avg `-0.0284` n `6`; index avg `-0.347` n `26`; metal avg `-0.2347` n `20`; unknown avg `0.6928` n `1024`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1728`, n `666`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.1455`, n `666`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1167`, n `666`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.1138`, n `666`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0981`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0742`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0709`, n `666`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0661`, n `668`, weak_sample_signal
