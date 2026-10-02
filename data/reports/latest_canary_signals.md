# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T23:22:27.016849+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0127` n `13`; crypto_alt avg `0.2279` n `235`; crypto_major avg `0.0583` n `8`; equity avg `-0.0035` n `143`; fx avg `-0.0004` n `6`; index avg `-0.0025` n `26`; metal avg `-0.002` n `20`; unknown avg `0.02` n `984`
- 1h: commodity avg `0.0047` n `13`; crypto_alt avg `0.7571` n `235`; crypto_major avg `0.4235` n `8`; equity avg `0.0205` n `143`; fx avg `0.0057` n `6`; index avg `-0.0046` n `26`; metal avg `0.0055` n `20`; unknown avg `0.2774` n `982`
- 4h: commodity avg `0.3201` n `13`; crypto_alt avg `1.3693` n `235`; crypto_major avg `0.8473` n `8`; equity avg `0.1111` n `143`; fx avg `-0.0191` n `6`; index avg `0.0165` n `26`; metal avg `0.0073` n `20`; unknown avg `0.3249` n `906`
- 24h: commodity avg `0.1289` n `13`; crypto_alt avg `-0.588` n `235`; crypto_major avg `-0.441` n `8`; equity avg `0.6644` n `142`; fx avg `-0.1387` n `6`; index avg `0.2718` n `26`; metal avg `-0.2545` n `20`; unknown avg `-0.6066` n `826`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1682`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1627`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1396`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.122`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1197`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.107`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0988`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
