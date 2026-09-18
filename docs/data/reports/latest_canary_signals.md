# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T09:22:28.797433+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0108` n `12`; crypto_alt avg `0.0831` n `234`; crypto_major avg `0.1063` n `8`; equity avg `0.0265` n `140`; fx avg `-0.0271` n `6`; index avg `0.0046` n `26`; metal avg `-0.0044` n `20`; unknown avg `0.0055` n `927`
- 1h: commodity avg `-0.0673` n `12`; crypto_alt avg `0.4127` n `234`; crypto_major avg `0.4163` n `8`; equity avg `-0.083` n `140`; fx avg `-0.0224` n `6`; index avg `-0.0287` n `26`; metal avg `0.021` n `20`; unknown avg `0.3964` n `919`
- 4h: commodity avg `-0.1898` n `12`; crypto_alt avg `1.0879` n `234`; crypto_major avg `1.0298` n `8`; equity avg `0.3583` n `140`; fx avg `0.0244` n `6`; index avg `0.0376` n `26`; metal avg `0.269` n `20`; unknown avg `0.0727` n `863`
- 24h: commodity avg `-0.3329` n `12`; crypto_alt avg `5.3405` n `234`; crypto_major avg `3.962` n `8`; equity avg `1.8418` n `140`; fx avg `0.1695` n `6`; index avg `0.2733` n `26`; metal avg `0.765` n `20`; unknown avg `2.5238` n `731`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1344`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1231`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.123`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1203`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1177`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1094`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1091`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
