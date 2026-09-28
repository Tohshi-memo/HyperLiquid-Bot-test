# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T03:22:30.435317+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.1017` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0117` n `12`; crypto_alt avg `-0.2822` n `234`; crypto_major avg `-0.1547` n `8`; equity avg `-0.1215` n `141`; fx avg `0.0074` n `6`; index avg `-0.0074` n `26`; metal avg `-0.0493` n `20`; unknown avg `-0.2257` n `956`
- 1h: commodity avg `-0.1125` n `12`; crypto_alt avg `-0.9854` n `234`; crypto_major avg `-0.4081` n `8`; equity avg `-0.2629` n `141`; fx avg `-0.0173` n `6`; index avg `-0.0146` n `26`; metal avg `-0.1621` n `20`; unknown avg `286.7401` n `952`
- 4h: commodity avg `-0.0623` n `12`; crypto_alt avg `-1.6654` n `234`; crypto_major avg `-1.2059` n `8`; equity avg `-1.3281` n `141`; fx avg `0.0855` n `6`; index avg `-0.1042` n `26`; metal avg `-0.553` n `20`; unknown avg `99.3258` n `936`
- 24h: commodity avg `-0.4613` n `12`; crypto_alt avg `-0.9635` n `234`; crypto_major avg `-1.2494` n `8`; equity avg `-1.4398` n `141`; fx avg `0.0698` n `6`; index avg `-0.1456` n `26`; metal avg `-0.7215` n `20`; unknown avg `12.2089` n `811`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1861`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1832`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1626`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1363`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.1355`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1238`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1212`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1174`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1173`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
