# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-04T20:23:11.771347+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0839` n `12`; crypto_alt avg `-0.0817` n `230`; crypto_major avg `-0.1893` n `8`; equity avg `-0.759` n `107`; fx avg `0.003` n `6`; index avg `-0.0946` n `25`; metal avg `-0.0282` n `20`; unknown avg `0.0737` n `782`
- 1h: commodity avg `-0.103` n `12`; crypto_alt avg `-0.1655` n `230`; crypto_major avg `-0.1606` n `8`; equity avg `-0.8092` n `107`; fx avg `-0.0029` n `6`; index avg `-0.0899` n `25`; metal avg `-0.0839` n `20`; unknown avg `0.0615` n `782`
- 4h: commodity avg `-0.0987` n `12`; crypto_alt avg `0.2323` n `230`; crypto_major avg `0.0372` n `8`; equity avg `-0.4121` n `107`; fx avg `0.0671` n `6`; index avg `0.0951` n `25`; metal avg `-0.0757` n `20`; unknown avg `-0.1722` n `782`
- 24h: commodity avg `-1.2527` n `12`; crypto_alt avg `-0.2618` n `230`; crypto_major avg `0.0706` n `8`; equity avg `3.0095` n `107`; fx avg `0.1379` n `6`; index avg `0.7346` n `25`; metal avg `0.8861` n `20`; unknown avg `0.4605` n `764`

## Correlations

- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1698`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1522`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1467`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1372`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1229`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1108`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.1055`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1001`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.0951`, n `668`, weak_sample_signal
