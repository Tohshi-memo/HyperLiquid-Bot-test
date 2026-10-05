# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-05T23:52:30.962264+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0135` n `13`; crypto_alt avg `0.0623` n `235`; crypto_major avg `-0.0247` n `8`; equity avg `-0.0029` n `144`; fx avg `0.0153` n `6`; index avg `-0.0067` n `26`; metal avg `-0.0231` n `20`; unknown avg `0.7148` n `1079`
- 1h: commodity avg `-0.0348` n `13`; crypto_alt avg `-0.2821` n `235`; crypto_major avg `-0.2353` n `8`; equity avg `0.0295` n `144`; fx avg `0.0122` n `6`; index avg `-0.0003` n `26`; metal avg `-0.0609` n `20`; unknown avg `0.6077` n `1077`
- 4h: commodity avg `0.0253` n `13`; crypto_alt avg `0.61` n `235`; crypto_major avg `0.2318` n `8`; equity avg `0.1862` n `144`; fx avg `0.0174` n `6`; index avg `0.0251` n `26`; metal avg `-0.0422` n `20`; unknown avg `-0.1543` n `979`
- 24h: commodity avg `-0.1799` n `13`; crypto_alt avg `0.2904` n `235`; crypto_major avg `-0.0729` n `8`; equity avg `0.2404` n `144`; fx avg `-0.0595` n `6`; index avg `0.1272` n `26`; metal avg `0.0738` n `20`; unknown avg `627.2712` n `798`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1962`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1778`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1701`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1038`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0989`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0973`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.097`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0941`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.0899`, n `668`, weak_sample_signal
