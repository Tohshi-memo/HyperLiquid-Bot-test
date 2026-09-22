# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T22:07:28.664170+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0001` n `12`; crypto_alt avg `-0.2515` n `234`; crypto_major avg `-0.2871` n `8`; equity avg `0.0395` n `140`; fx avg `0.0036` n `6`; index avg `0.0029` n `26`; metal avg `0.028` n `20`; unknown avg `0.2987` n `942`
- 1h: commodity avg `0.0121` n `12`; crypto_alt avg `-0.0323` n `234`; crypto_major avg `-0.1771` n `8`; equity avg `0.0539` n `140`; fx avg `-0.0035` n `6`; index avg `0.0049` n `26`; metal avg `0.0253` n `20`; unknown avg `0.0539` n `942`
- 4h: commodity avg `0.204` n `12`; crypto_alt avg `0.391` n `234`; crypto_major avg `-0.076` n `8`; equity avg `0.1759` n `140`; fx avg `-0.0157` n `6`; index avg `0.0029` n `26`; metal avg `0.0824` n `20`; unknown avg `0.8719` n `906`
- 24h: commodity avg `0.24` n `12`; crypto_alt avg `2.21` n `234`; crypto_major avg `-0.1198` n `8`; equity avg `0.8539` n `140`; fx avg `-0.2964` n `6`; index avg `0.1102` n `26`; metal avg `0.2649` n `20`; unknown avg `1.8951` n `836`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1227`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1226`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1155`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.1095`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1067`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.098`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.0968`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0944`, n `668`, weak_sample_signal
