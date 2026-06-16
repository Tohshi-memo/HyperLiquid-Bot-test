# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-16T13:37:41.815233+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 1h_index_leads_crypto: score `1.1253` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.4433` n `12`; crypto_alt avg `-0.0247` n `228`; crypto_major avg `-0.1389` n `8`; equity avg `0.2396` n `77`; fx avg `0.0079` n `6`; index avg `0.166` n `23`; metal avg `0.1353` n `18`; unknown avg `0.067` n `687`
- 1h: commodity avg `0.6637` n `12`; crypto_alt avg `-1.1732` n `228`; crypto_major avg `-0.9859` n `8`; equity avg `0.0192` n `77`; fx avg `0.009` n `6`; index avg `0.1394` n `23`; metal avg `-0.0315` n `18`; unknown avg `0.542` n `687`
- 4h: commodity avg `0.133` n `12`; crypto_alt avg `-0.7099` n `228`; crypto_major avg `-0.1486` n `8`; equity avg `-0.3354` n `77`; fx avg `0.005` n `6`; index avg `0.084` n `23`; metal avg `0.1244` n `18`; unknown avg `0.535` n `687`
- 24h: commodity avg `-0.0194` n `12`; crypto_alt avg `-1.6539` n `228`; crypto_major avg `0.3512` n `8`; equity avg `0.9651` n `77`; fx avg `-0.0788` n `6`; index avg `0.2917` n `23`; metal avg `-0.1867` n `18`; unknown avg `0.4461` n `623`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.091`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.073`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0655`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0639`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0638`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0558`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.0558`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0543`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.047`, n `668`, weak_sample_signal
