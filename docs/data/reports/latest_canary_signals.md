# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-19T16:52:26.948247+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0115` n `12`; crypto_alt avg `0.1301` n `234`; crypto_major avg `-0.0028` n `8`; equity avg `-0.005` n `140`; fx avg `0.0006` n `6`; index avg `0.0023` n `26`; metal avg `0.0033` n `20`; unknown avg `0.4165` n `935`
- 1h: commodity avg `-0.0042` n `12`; crypto_alt avg `0.4576` n `234`; crypto_major avg `0.0468` n `8`; equity avg `0.0053` n `140`; fx avg `-0.0021` n `6`; index avg `0.0071` n `26`; metal avg `-0.013` n `20`; unknown avg `4.2715` n `917`
- 4h: commodity avg `-0.1546` n `12`; crypto_alt avg `0.2425` n `234`; crypto_major avg `0.2004` n `8`; equity avg `0.0295` n `140`; fx avg `-0.0094` n `6`; index avg `0.0143` n `26`; metal avg `-0.0024` n `20`; unknown avg `5.0532` n `914`
- 24h: commodity avg `-0.0988` n `12`; crypto_alt avg `3.1076` n `234`; crypto_major avg `1.6234` n `8`; equity avg `0.6555` n `140`; fx avg `0.0204` n `6`; index avg `0.1609` n `26`; metal avg `-0.0613` n `20`; unknown avg `1.8861` n `798`

## Correlations

- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1761`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1748`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1716`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1598`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.157`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1457`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1372`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1294`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1293`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
