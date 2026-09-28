# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T21:37:36.975502+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1251` n `12`; crypto_alt avg `-0.1025` n `234`; crypto_major avg `-0.0337` n `8`; equity avg `-0.0149` n `141`; fx avg `-0.0108` n `6`; index avg `-0.0033` n `26`; metal avg `-0.0152` n `20`; unknown avg `2.5117` n `963`
- 1h: commodity avg `0.1042` n `12`; crypto_alt avg `-0.2824` n `234`; crypto_major avg `-0.2418` n `8`; equity avg `0.0728` n `141`; fx avg `-0.0027` n `6`; index avg `0.0204` n `26`; metal avg `-0.0057` n `20`; unknown avg `7.927` n `959`
- 4h: commodity avg `0.3237` n `12`; crypto_alt avg `-0.7509` n `234`; crypto_major avg `-0.8199` n `8`; equity avg `-0.2099` n `141`; fx avg `-0.0078` n `6`; index avg `-0.0284` n `26`; metal avg `-0.215` n `20`; unknown avg `0.6183` n `857`
- 24h: commodity avg `-0.1818` n `12`; crypto_alt avg `-3.6897` n `234`; crypto_major avg `-1.9402` n `8`; equity avg `-3.3145` n `141`; fx avg `0.0759` n `6`; index avg `-0.3142` n `26`; metal avg `-1.154` n `20`; unknown avg `26.1778` n `796`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1745`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1599`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1285`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1145`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1128`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1075`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1058`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1052`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0954`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.0943`, n `668`, weak_sample_signal
