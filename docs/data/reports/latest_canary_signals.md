# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-02T03:37:32.685452+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0139` n `12`; crypto_alt avg `-0.1343` n `232`; crypto_major avg `-0.0084` n `8`; equity avg `-0.0635` n `132`; fx avg `-0.0053` n `6`; index avg `-0.022` n `26`; metal avg `-0.07` n `20`; unknown avg `-0.131` n `792`
- 1h: commodity avg `-0.0443` n `12`; crypto_alt avg `0.3887` n `232`; crypto_major avg `0.4003` n `8`; equity avg `-0.0122` n `132`; fx avg `-0.0007` n `6`; index avg `-0.019` n `26`; metal avg `-0.1412` n `20`; unknown avg `0.324` n `790`
- 4h: commodity avg `0.0366` n `12`; crypto_alt avg `0.372` n `232`; crypto_major avg `0.0299` n `8`; equity avg `-0.1583` n `132`; fx avg `-0.0737` n `6`; index avg `-0.0389` n `26`; metal avg `-0.315` n `20`; unknown avg `2.2186` n `790`
- 24h: commodity avg `0.8602` n `12`; crypto_alt avg `-0.8002` n `232`; crypto_major avg `-1.8544` n `8`; equity avg `-2.3617` n `130`; fx avg `-0.0493` n `6`; index avg `-0.4254` n `26`; metal avg `-1.1659` n `20`; unknown avg `-0.0722` n `752`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.0791`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.0702`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0569`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0517`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0485`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0432`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0379`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0333`, n `668`, weak_sample_signal
