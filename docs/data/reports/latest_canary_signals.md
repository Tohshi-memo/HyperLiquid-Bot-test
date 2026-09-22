# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-22T18:22:37.752052+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1256` n `12`; crypto_alt avg `0.2351` n `234`; crypto_major avg `0.1755` n `8`; equity avg `0.0952` n `140`; fx avg `0.0153` n `6`; index avg `0.0138` n `26`; metal avg `0.0244` n `20`; unknown avg `-0.1877` n `942`
- 1h: commodity avg `-0.162` n `12`; crypto_alt avg `0.2539` n `234`; crypto_major avg `0.0574` n `8`; equity avg `0.2776` n `140`; fx avg `0.006` n `6`; index avg `0.0745` n `26`; metal avg `0.2319` n `20`; unknown avg `-0.1613` n `940`
- 4h: commodity avg `0.033` n `12`; crypto_alt avg `1.1278` n `234`; crypto_major avg `0.3916` n `8`; equity avg `0.1288` n `140`; fx avg `0.0132` n `6`; index avg `0.0294` n `26`; metal avg `0.215` n `20`; unknown avg `0.3136` n `880`
- 24h: commodity avg `-0.0024` n `12`; crypto_alt avg `2.5752` n `234`; crypto_major avg `1.1742` n `8`; equity avg `0.8382` n `140`; fx avg `-0.2719` n `6`; index avg `0.1308` n `26`; metal avg `0.2368` n `20`; unknown avg `0.735` n `796`

## Correlations

- news_risk_score -> fx_forward_1h_return_pct: corr `0.1383`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `-0.1238`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.115`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `-0.1134`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.113`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.1064`, n `668`, weak_sample_signal
- market_context_score -> index_forward_1h_return_pct: corr `0.101`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `0.1002`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `-0.0986`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `0.0967`, n `668`, weak_sample_signal
