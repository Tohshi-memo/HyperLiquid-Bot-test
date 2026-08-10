# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-10T14:46:44.311221+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0158` n `12`; crypto_alt avg `-0.0872` n `230`; crypto_major avg `-0.0636` n `8`; equity avg `-0.0828` n `113`; fx avg `0.0063` n `6`; index avg `-0.0046` n `25`; metal avg `0.0353` n `20`; unknown avg `0.0681` n `784`
- 1h: commodity avg `-0.0006` n `12`; crypto_alt avg `0.0205` n `230`; crypto_major avg `0.3348` n `8`; equity avg `0.357` n `113`; fx avg `0.0147` n `6`; index avg `0.0706` n `25`; metal avg `0.2598` n `20`; unknown avg `0.2135` n `784`
- 4h: commodity avg `0.3446` n `12`; crypto_alt avg `-0.1977` n `230`; crypto_major avg `-0.3145` n `8`; equity avg `-0.5557` n `113`; fx avg `0.0513` n `6`; index avg `-0.0155` n `25`; metal avg `0.1235` n `20`; unknown avg `0.2762` n `784`
- 24h: commodity avg `0.9832` n `12`; crypto_alt avg `0.2418` n `230`; crypto_major avg `-0.6065` n `8`; equity avg `-0.8245` n `113`; fx avg `0.27` n `6`; index avg `0.0295` n `25`; metal avg `-0.0455` n `20`; unknown avg `103.7283` n `752`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1654`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1549`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.151`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1414`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.1381`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1344`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1275`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1175`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1156`, n `668`, weak_sample_signal
