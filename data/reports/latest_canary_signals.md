# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-07T16:07:27.428712+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_crypto_equity_divergence: score `1.6598` - Crypto majors and equity perps are diverging; watch lead/lag rotation.

## Class Returns

- 15m: commodity avg `0.0067` n `12`; crypto_alt avg `-0.1709` n `229`; crypto_major avg `-0.2014` n `8`; equity avg `0.2575` n `91`; fx avg `-0.0101` n `6`; index avg `0.054` n `25`; metal avg `0.0177` n `20`; unknown avg `0.1161` n `763`
- 1h: commodity avg `0.0708` n `12`; crypto_alt avg `0.446` n `229`; crypto_major avg `0.4326` n `8`; equity avg `0.4014` n `91`; fx avg `-0.0445` n `6`; index avg `0.0816` n `25`; metal avg `-0.0565` n `20`; unknown avg `-0.0298` n `755`
- 4h: commodity avg `0.5129` n `12`; crypto_alt avg `-0.3609` n `229`; crypto_major avg `0.0928` n `8`; equity avg `-1.567` n `91`; fx avg `-0.0413` n `6`; index avg `-0.1872` n `25`; metal avg `-0.2548` n `20`; unknown avg `-0.1769` n `755`
- 24h: commodity avg `0.5484` n `12`; crypto_alt avg `-0.5579` n `229`; crypto_major avg `-0.0238` n `8`; equity avg `-3.4933` n `91`; fx avg `-0.2304` n `6`; index avg `-0.6547` n `25`; metal avg `-0.0652` n `20`; unknown avg `-0.0297` n `731`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1186`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.096`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `-0.0852`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.0849`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0801`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0743`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0682`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0621`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0536`, n `668`, weak_sample_signal
