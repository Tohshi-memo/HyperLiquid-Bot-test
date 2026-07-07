# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T17:22:26.649884+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.27` - Polymarket crypto volume is unusually high.
- 4h_crypto_equity_divergence: score `1.6282` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0422` n `12`; crypto_alt avg `-0.1789` n `229`; crypto_major avg `-0.1336` n `8`; equity avg `-0.0928` n `91`; fx avg `0.0008` n `6`; index avg `0.0112` n `25`; metal avg `-0.0524` n `20`; unknown avg `0.2096` n `763`
- 1h: commodity avg `0.0616` n `12`; crypto_alt avg `-0.1014` n `229`; crypto_major avg `-0.0455` n `8`; equity avg `0.0359` n `91`; fx avg `0.0077` n `6`; index avg `0.039` n `25`; metal avg `-0.0567` n `20`; unknown avg `-0.0536` n `763`
- 4h: commodity avg `0.3566` n `12`; crypto_alt avg `0.3457` n `229`; crypto_major avg `0.9579` n `8`; equity avg `-0.6703` n `91`; fx avg `-0.0361` n `6`; index avg `-0.0407` n `25`; metal avg `-0.1565` n `20`; unknown avg `0.652` n `755`
- 24h: commodity avg `0.7393` n `12`; crypto_alt avg `-0.8106` n `229`; crypto_major avg `-0.3284` n `8`; equity avg `-2.9335` n `91`; fx avg `-0.2495` n `6`; index avg `-0.5071` n `25`; metal avg `-0.0983` n `20`; unknown avg `0.26` n `731`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1206`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0876`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0854`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0734`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0656`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0641`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0549`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0505`, n `668`, weak_sample_signal
