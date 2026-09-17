# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T06:07:26.323998+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0532` n `12`; crypto_alt avg `-0.024` n `234`; crypto_major avg `-0.0553` n `8`; equity avg `-0.0011` n `137`; fx avg `0.0165` n `6`; index avg `0.0076` n `27`; metal avg `0.0501` n `20`; unknown avg `0.0342` n `899`
- 1h: commodity avg `-0.1515` n `12`; crypto_alt avg `0.052` n `234`; crypto_major avg `-0.1336` n `8`; equity avg `-0.2437` n `137`; fx avg `0.0023` n `6`; index avg `-0.0544` n `27`; metal avg `0.0424` n `20`; unknown avg `0.1014` n `899`
- 4h: commodity avg `-0.1511` n `12`; crypto_alt avg `0.7504` n `234`; crypto_major avg `0.2` n `8`; equity avg `0.095` n `137`; fx avg `-0.0057` n `6`; index avg `-0.0141` n `27`; metal avg `0.1767` n `20`; unknown avg `0.1406` n `889`
- 24h: commodity avg `-0.5495` n `12`; crypto_alt avg `2.4435` n `234`; crypto_major avg `1.1432` n `8`; equity avg `0.831` n `137`; fx avg `0.0178` n `6`; index avg `0.0276` n `27`; metal avg `-0.1087` n `20`; unknown avg `0.2725` n `721`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1354`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1123`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1011`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.099`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0958`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0804`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.077`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0755`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
