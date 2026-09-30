# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-30T02:22:31.284783+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0125` n `12`; crypto_alt avg `-0.2718` n `234`; crypto_major avg `-0.173` n `8`; equity avg `-0.1233` n `142`; fx avg `-0.0342` n `6`; index avg `-0.0026` n `26`; metal avg `0.0257` n `20`; unknown avg `2.8683` n `963`
- 1h: commodity avg `-0.0904` n `12`; crypto_alt avg `-0.0986` n `234`; crypto_major avg `0.0933` n `8`; equity avg `-0.099` n `142`; fx avg `-0.0558` n `6`; index avg `-0.0058` n `26`; metal avg `0.0188` n `20`; unknown avg `7.4793` n `961`
- 4h: commodity avg `0.1099` n `12`; crypto_alt avg `0.2637` n `234`; crypto_major avg `0.0456` n `8`; equity avg `-0.1831` n `142`; fx avg `-0.0574` n `6`; index avg `-0.0497` n `26`; metal avg `-0.0937` n `20`; unknown avg `6.837` n `954`
- 24h: commodity avg `-0.9237` n `12`; crypto_alt avg `3.0509` n `234`; crypto_major avg `1.1488` n `8`; equity avg `0.9145` n `142`; fx avg `-0.2054` n `6`; index avg `0.1127` n `26`; metal avg `0.2024` n `20`; unknown avg `3258.0514` n `834`

## Correlations

- market_context_score -> equity_forward_1h_return_pct: corr `-0.1793`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1785`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1723`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1513`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1281`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1257`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `-0.1249`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1217`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1103`, n `668`, weak_sample_signal
