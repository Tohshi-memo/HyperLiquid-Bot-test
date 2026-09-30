# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T06:37:32.633741+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0693` n `12`; crypto_alt avg `-0.3793` n `234`; crypto_major avg `-0.1895` n `8`; equity avg `-0.0526` n `142`; fx avg `0.0045` n `6`; index avg `-0.0147` n `26`; metal avg `-0.0012` n `20`; unknown avg `1.6468` n `963`
- 1h: commodity avg `0.0316` n `12`; crypto_alt avg `-0.7272` n `234`; crypto_major avg `-0.5239` n `8`; equity avg `-0.1829` n `142`; fx avg `0.0185` n `6`; index avg `-0.0382` n `26`; metal avg `0.0536` n `20`; unknown avg `1.6621` n `931`
- 4h: commodity avg `0.04` n `12`; crypto_alt avg `-0.2818` n `234`; crypto_major avg `-0.402` n `8`; equity avg `0.0143` n `142`; fx avg `0.0837` n `6`; index avg `0.0394` n `26`; metal avg `0.0549` n `20`; unknown avg `4.1793` n `925`
- 24h: commodity avg `-0.8924` n `12`; crypto_alt avg `0.2402` n `234`; crypto_major avg `-0.9187` n `8`; equity avg `0.4391` n `142`; fx avg `-0.0794` n `6`; index avg `0.0701` n `26`; metal avg `0.1851` n `20`; unknown avg `2855.7918` n `826`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1747`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1638`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1509`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.147`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1264`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1178`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1137`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1114`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1104`, n `668`, weak_sample_signal
