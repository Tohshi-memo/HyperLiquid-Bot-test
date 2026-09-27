# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-27T11:52:26.775189+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0034` n `12`; crypto_alt avg `-0.0077` n `234`; crypto_major avg `0.0609` n `8`; equity avg `-0.002` n `141`; fx avg `-0.0014` n `6`; index avg `0.0025` n `26`; metal avg `0.0026` n `20`; unknown avg `0.8283` n `962`
- 1h: commodity avg `0.0264` n `12`; crypto_alt avg `-0.095` n `234`; crypto_major avg `0.089` n `8`; equity avg `-0.0016` n `141`; fx avg `-0.005` n `6`; index avg `-0.0094` n `26`; metal avg `-0.0027` n `20`; unknown avg `0.6152` n `960`
- 4h: commodity avg `0.0519` n `12`; crypto_alt avg `-0.2769` n `234`; crypto_major avg `0.2017` n `8`; equity avg `0.0766` n `141`; fx avg `-0.0174` n `6`; index avg `0.0084` n `26`; metal avg `-0.0121` n `20`; unknown avg `2.0358` n `943`
- 24h: commodity avg `0.0862` n `12`; crypto_alt avg `0.6278` n `234`; crypto_major avg `0.6081` n `8`; equity avg `0.3377` n `141`; fx avg `-0.0457` n `6`; index avg `0.0261` n `26`; metal avg `-0.0039` n `20`; unknown avg `9.1445` n `887`

## Correlations

- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1622`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1505`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1499`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1427`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1403`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1243`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1159`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0971`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0903`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0879`, n `668`, weak_sample_signal
