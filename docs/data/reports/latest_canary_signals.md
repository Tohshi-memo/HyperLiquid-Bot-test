# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T10:22:29.563363+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0264` n `12`; crypto_alt avg `0.0806` n `234`; crypto_major avg `0.0837` n `8`; equity avg `0.0653` n `140`; fx avg `-0.0074` n `6`; index avg `0.0209` n `26`; metal avg `-0.0085` n `20`; unknown avg `-0.4304` n `927`
- 1h: commodity avg `0.1172` n `12`; crypto_alt avg `0.2947` n `234`; crypto_major avg `0.0621` n `8`; equity avg `-0.1128` n `140`; fx avg `0.0396` n `6`; index avg `-0.0342` n `26`; metal avg `-0.1089` n `20`; unknown avg `0.2512` n `925`
- 4h: commodity avg `0.0062` n `12`; crypto_alt avg `1.2945` n `234`; crypto_major avg `0.9186` n `8`; equity avg `0.0449` n `140`; fx avg `0.1249` n `6`; index avg `-0.0046` n `26`; metal avg `0.0372` n `20`; unknown avg `0.0633` n `901`
- 24h: commodity avg `-0.0969` n `12`; crypto_alt avg `6.2103` n `234`; crypto_major avg `4.8025` n `8`; equity avg `1.6748` n `140`; fx avg `0.1829` n `6`; index avg `0.2061` n `26`; metal avg `0.657` n `20`; unknown avg `2.8849` n `731`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1407`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1222`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1212`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1179`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1138`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1099`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1093`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1053`, n `668`, weak_sample_signal
