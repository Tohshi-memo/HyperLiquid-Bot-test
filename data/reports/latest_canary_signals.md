# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-02T12:07:33.890291+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0475` n `13`; crypto_alt avg `-0.0036` n `234`; crypto_major avg `-0.073` n `8`; equity avg `-0.0046` n `142`; fx avg `0.0133` n `6`; index avg `-0.0139` n `26`; metal avg `-0.0496` n `20`; unknown avg `0.5558` n `977`
- 1h: commodity avg `0.1037` n `13`; crypto_alt avg `0.0103` n `234`; crypto_major avg `-0.1444` n `8`; equity avg `-0.2543` n `142`; fx avg `-0.0117` n `6`; index avg `-0.0484` n `26`; metal avg `-0.0933` n `20`; unknown avg `0.0395` n `977`
- 4h: commodity avg `0.037` n `13`; crypto_alt avg `0.0863` n `234`; crypto_major avg `0.2257` n `8`; equity avg `-0.2952` n `142`; fx avg `-0.0311` n `6`; index avg `-0.025` n `26`; metal avg `-0.1728` n `20`; unknown avg `0.1901` n `963`
- 24h: commodity avg `-0.489` n `13`; crypto_alt avg `1.7946` n `234`; crypto_major avg `1.7346` n `8`; equity avg `0.8329` n `142`; fx avg `-0.3488` n `6`; index avg `0.1447` n `26`; metal avg `-0.1156` n `20`; unknown avg `-0.1627` n `795`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `-0.173`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1628`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1304`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1272`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1258`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1237`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1077`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1008`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0984`, n `668`, weak_sample_signal
