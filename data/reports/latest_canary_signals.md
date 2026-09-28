# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T10:07:31.587491+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1021` n `12`; crypto_alt avg `0.2546` n `234`; crypto_major avg `0.2142` n `8`; equity avg `-0.0517` n `141`; fx avg `0.0082` n `6`; index avg `-0.0191` n `26`; metal avg `0.016` n `20`; unknown avg `25.019` n `960`
- 1h: commodity avg `0.1188` n `12`; crypto_alt avg `0.2355` n `234`; crypto_major avg `0.3573` n `8`; equity avg `0.0824` n `141`; fx avg `-0.0151` n `6`; index avg `0.0107` n `26`; metal avg `0.0999` n `20`; unknown avg `23.3516` n `960`
- 4h: commodity avg `0.3536` n `12`; crypto_alt avg `-1.5041` n `234`; crypto_major avg `-0.3213` n `8`; equity avg `-1.1543` n `141`; fx avg `-0.0883` n `6`; index avg `-0.0954` n `26`; metal avg `-0.1288` n `20`; unknown avg `9.5702` n `942`
- 24h: commodity avg `0.0352` n `12`; crypto_alt avg `-4.3493` n `234`; crypto_major avg `-3.1817` n `8`; equity avg `-2.8632` n `141`; fx avg `0.0187` n `6`; index avg `-0.2886` n `26`; metal avg `-0.9019` n `20`; unknown avg `7.0595` n `814`

## Correlations

- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1682`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1475`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1351`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1308`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1054`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1053`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1038`, n `668`, weak_sample_signal
