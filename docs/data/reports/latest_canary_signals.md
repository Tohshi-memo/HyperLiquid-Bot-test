# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-16T19:22:29.779685+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.67` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `2.0393` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `-0.01` n `12`; crypto_alt avg `-0.7916` n `234`; crypto_major avg `-0.745` n `8`; equity avg `-0.649` n `137`; fx avg `0.0205` n `6`; index avg `-0.1323` n `27`; metal avg `-0.1496` n `20`; unknown avg `4.1352` n `917`
- 1h: commodity avg `0.0537` n `12`; crypto_alt avg `-0.4738` n `234`; crypto_major avg `-0.6044` n `8`; equity avg `-1.5702` n `137`; fx avg `0.0524` n `6`; index avg `-0.3718` n `27`; metal avg `-0.5094` n `20`; unknown avg `14.0608` n `887`
- 4h: commodity avg `0.0712` n `12`; crypto_alt avg `0.2441` n `234`; crypto_major avg `0.1576` n `8`; equity avg `-1.8817` n `137`; fx avg `0.0265` n `6`; index avg `-0.4271` n `27`; metal avg `-0.7661` n `20`; unknown avg `14.614` n `875`
- 24h: commodity avg `-0.5397` n `12`; crypto_alt avg `-1.6152` n `234`; crypto_major avg `-0.5992` n `8`; equity avg `-0.4037` n `137`; fx avg `0.0536` n `6`; index avg `-0.1373` n `27`; metal avg `-0.476` n `20`; unknown avg `6.0841` n `799`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1228`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1028`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.0935`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0905`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0884`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.0648`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0557`, n `668`, weak_sample_signal
