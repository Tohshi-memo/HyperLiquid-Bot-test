# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-12T07:52:27.989567+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1675` n `13`; crypto_alt avg `0.0653` n `235`; crypto_major avg `0.026` n `8`; equity avg `0.0483` n `151`; fx avg `-0.0185` n `6`; index avg `0.0212` n `26`; metal avg `-0.0167` n `20`; unknown avg `7.2253` n `1133`
- 1h: commodity avg `0.0138` n `13`; crypto_alt avg `0.0476` n `235`; crypto_major avg `0.0973` n `8`; equity avg `0.1242` n `151`; fx avg `-0.0388` n `6`; index avg `0.0429` n `26`; metal avg `0.0252` n `20`; unknown avg `7.3835` n `1131`
- 4h: commodity avg `0.2273` n `13`; crypto_alt avg `0.2942` n `235`; crypto_major avg `0.6292` n `8`; equity avg `-0.2494` n `151`; fx avg `-0.0223` n `6`; index avg `-0.0318` n `26`; metal avg `-0.0581` n `20`; unknown avg `5.6038` n `1043`
- 24h: commodity avg `-0.2527` n `13`; crypto_alt avg `2.5764` n `235`; crypto_major avg `1.9832` n `8`; equity avg `-0.49` n `151`; fx avg `-0.0941` n `6`; index avg `-0.0248` n `26`; metal avg `0.0899` n `20`; unknown avg `2.9049` n `866`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.2101`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1772`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1148`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1101`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0836`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0827`, n `668`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `-0.0802`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0784`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0778`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.075`, n `668`, weak_sample_signal
