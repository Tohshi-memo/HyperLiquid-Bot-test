# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-28T18:52:37.475050+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `2.3137` - Commodity perps and crypto are moving differently; check macro-linked stress.
- 4h_crypto_metal_divergence: score `1.6311` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0051` n `12`; crypto_alt avg `0.1713` n `234`; crypto_major avg `0.2311` n `8`; equity avg `0.1184` n `141`; fx avg `-0.0034` n `6`; index avg `0.0089` n `26`; metal avg `0.0132` n `20`; unknown avg `-0.0009` n `963`
- 1h: commodity avg `0.0247` n `12`; crypto_alt avg `0.1412` n `234`; crypto_major avg `0.1812` n `8`; equity avg `0.0579` n `141`; fx avg `-0.0101` n `6`; index avg `-0.0038` n `26`; metal avg `-0.0337` n `20`; unknown avg `0.6215` n `961`
- 4h: commodity avg `-0.4799` n `12`; crypto_alt avg `2.0313` n `234`; crypto_major avg `1.8338` n `8`; equity avg `1.1347` n `141`; fx avg `0.0082` n `6`; index avg `0.1909` n `26`; metal avg `0.2027` n `20`; unknown avg `18.2823` n `954`
- 24h: commodity avg `-0.5096` n `12`; crypto_alt avg `-3.2662` n `234`; crypto_major avg `-1.5136` n `8`; equity avg `-2.942` n `141`; fx avg `0.0372` n `6`; index avg `-0.2656` n `26`; metal avg `-0.9748` n `20`; unknown avg `22.9349` n `786`

## Correlations

- market_context_score -> unknown_forward_1h_return_pct: corr `0.1788`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1637`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.1306`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1248`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1197`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1144`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `0.1127`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.1083`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1074`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0988`, n `668`, weak_sample_signal
