# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T09:52:35.634174+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0813` n `12`; crypto_alt avg `-0.0227` n `230`; crypto_major avg `-0.0769` n `8`; equity avg `-0.0711` n `108`; fx avg `0.0084` n `6`; index avg `-0.0215` n `25`; metal avg `-0.0193` n `20`; unknown avg `-0.0183` n `781`
- 1h: commodity avg `0.0323` n `12`; crypto_alt avg `0.0437` n `230`; crypto_major avg `-0.0507` n `8`; equity avg `0.1718` n `108`; fx avg `0.0059` n `6`; index avg `0.0027` n `25`; metal avg `0.0274` n `20`; unknown avg `0.616` n `781`
- 4h: commodity avg `0.3877` n `12`; crypto_alt avg `-0.1155` n `230`; crypto_major avg `-0.0552` n `8`; equity avg `-0.9072` n `108`; fx avg `0.0373` n `6`; index avg `-0.1233` n `25`; metal avg `-0.1194` n `20`; unknown avg `0.6882` n `749`
- 24h: commodity avg `-1.3086` n `12`; crypto_alt avg `0.7595` n `230`; crypto_major avg `1.0604` n `8`; equity avg `2.7988` n `108`; fx avg `-0.0294` n `6`; index avg `0.6549` n `25`; metal avg `1.1309` n `20`; unknown avg `0.151` n `748`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1517`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1258`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1256`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1131`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1109`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1086`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.1031`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1026`, n `668`, weak_sample_signal
