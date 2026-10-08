# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T02:07:25.921355+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0006` n `13`; crypto_alt avg `-0.0917` n `235`; crypto_major avg `-0.107` n `8`; equity avg `-0.0655` n `150`; fx avg `0.0043` n `6`; index avg `-0.0076` n `26`; metal avg `0.0274` n `20`; unknown avg `-0.019` n `1075`
- 1h: commodity avg `0.0772` n `13`; crypto_alt avg `-0.6196` n `235`; crypto_major avg `-0.4801` n `8`; equity avg `-0.0153` n `150`; fx avg `0.0269` n `6`; index avg `0.0424` n `26`; metal avg `0.0968` n `20`; unknown avg `0.573` n `1075`
- 4h: commodity avg `0.1054` n `13`; crypto_alt avg `0.81` n `235`; crypto_major avg `0.307` n `8`; equity avg `0.0256` n `150`; fx avg `-0.0251` n `6`; index avg `-0.0197` n `26`; metal avg `0.3701` n `20`; unknown avg `0.2729` n `1069`
- 24h: commodity avg `0.4219` n `13`; crypto_alt avg `-0.1567` n `235`; crypto_major avg `-0.9203` n `8`; equity avg `-0.6019` n `150`; fx avg `-0.1652` n `6`; index avg `-0.1455` n `26`; metal avg `-0.1369` n `20`; unknown avg `247.9875` n `980`

## Correlations

- risk_on_score -> fx_forward_1h_return_pct: corr `0.1485`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.134`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1003`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0856`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0843`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.079`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0771`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0666`, n `668`, weak_sample_signal
