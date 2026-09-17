# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-17T00:37:29.130153+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0272` n `12`; crypto_alt avg `-0.1583` n `234`; crypto_major avg `-0.123` n `8`; equity avg `0.0578` n `137`; fx avg `0.005` n `6`; index avg `0.0056` n `27`; metal avg `-0.0165` n `20`; unknown avg `2.2239` n `913`
- 1h: commodity avg `-0.0954` n `12`; crypto_alt avg `0.3862` n `234`; crypto_major avg `0.178` n `8`; equity avg `0.1751` n `137`; fx avg `-0.0101` n `6`; index avg `0.0589` n `27`; metal avg `0.0927` n `20`; unknown avg `1.3824` n `909`
- 4h: commodity avg `-0.0752` n `12`; crypto_alt avg `1.3746` n `234`; crypto_major avg `0.227` n `8`; equity avg `0.8839` n `137`; fx avg `-0.0381` n `6`; index avg `0.1587` n `27`; metal avg `0.1474` n `20`; unknown avg `1.6207` n `813`
- 24h: commodity avg `-0.6133` n `12`; crypto_alt avg `1.3588` n `234`; crypto_major avg `0.9532` n `8`; equity avg `1.5287` n `137`; fx avg `-0.0286` n `6`; index avg `0.1384` n `27`; metal avg `-0.0946` n `20`; unknown avg `0.2186` n `715`

## Correlations

- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1162`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.1043`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.104`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.099`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0946`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0864`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0786`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0732`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0719`, n `668`, weak_sample_signal
