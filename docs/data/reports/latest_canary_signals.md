# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T20:52:29.260812+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0301` n `12`; crypto_alt avg `-0.2381` n `234`; crypto_major avg `-0.1456` n `8`; equity avg `-0.0284` n `141`; fx avg `-0.0037` n `6`; index avg `-0.0006` n `26`; metal avg `-0.0278` n `20`; unknown avg `-0.5186` n `963`
- 1h: commodity avg `0.1442` n `12`; crypto_alt avg `0.244` n `234`; crypto_major avg `0.044` n `8`; equity avg `-0.0809` n `141`; fx avg `-0.0078` n `6`; index avg `-0.0093` n `26`; metal avg `-0.107` n `20`; unknown avg `-0.5238` n `899`
- 4h: commodity avg `0.1451` n `12`; crypto_alt avg `-0.5212` n `234`; crypto_major avg `-0.4563` n `8`; equity avg `-0.2198` n `141`; fx avg `-0.0002` n `6`; index avg `-0.0259` n `26`; metal avg `-0.1467` n `20`; unknown avg `3.9051` n `858`
- 24h: commodity avg `-0.2536` n `12`; crypto_alt avg `-3.726` n `234`; crypto_major avg `-2.0641` n `8`; equity avg `-3.3934` n `141`; fx avg `0.0493` n `6`; index avg `-0.3202` n `26`; metal avg `-1.1743` n `20`; unknown avg `25.6543` n `776`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1752`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1599`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1294`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1166`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1092`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1078`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0945`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0932`, n `668`, weak_sample_signal
