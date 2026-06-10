# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-10T19:52:52.221618+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.7436` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `-0.0006` n `12`; crypto_alt avg `-0.3592` n `228`; crypto_major avg `-0.2906` n `8`; equity avg `-0.0682` n `74`; fx avg `0.0018` n `6`; index avg `-0.0026` n `23`; metal avg `0.125` n `18`; unknown avg `-2.5135` n `550`
- 1h: commodity avg `0.038` n `12`; crypto_alt avg `-0.5198` n `228`; crypto_major avg `-0.1208` n `8`; equity avg `-0.1446` n `74`; fx avg `-0.0136` n `6`; index avg `-0.1218` n `23`; metal avg `-0.412` n `18`; unknown avg `-2.595` n `550`
- 4h: commodity avg `-0.4032` n `12`; crypto_alt avg `-2.117` n `228`; crypto_major avg `-2.3023` n `8`; equity avg `-0.8363` n `74`; fx avg `0.0026` n `6`; index avg `-0.5587` n `23`; metal avg `-0.8692` n `18`; unknown avg `-2.4225` n `548`
- 24h: commodity avg `1.0639` n `12`; crypto_alt avg `-1.9974` n `228`; crypto_major avg `-2.4021` n `8`; equity avg `-1.1858` n `74`; fx avg `-0.0301` n `6`; index avg `-0.9513` n `23`; metal avg `-2.0437` n `18`; unknown avg `-2.8442` n `537`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `-0.1022`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.087`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.0777`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.068`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0652`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0587`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.054`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0537`, n `668`, weak_sample_signal
