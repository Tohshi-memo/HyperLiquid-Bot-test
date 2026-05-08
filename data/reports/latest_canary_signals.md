# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-08T03:22:13.019213+00:00`
- Correlation status: `ready`
- Asset price records: `609`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.08` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0171` n `12`; crypto_alt avg `0.4751` n `228`; crypto_major avg `0.3004` n `8`; equity avg `-0.0526` n `65`; fx avg `-0.0037` n `5`; index avg `0.0063` n `23`; metal avg `0.0589` n `18`; unknown avg `0.0398` n `365`
- 1h: commodity avg `-0.1178` n `12`; crypto_alt avg `0.5181` n `228`; crypto_major avg `0.2713` n `8`; equity avg `-0.0655` n `65`; fx avg `-0.0121` n `5`; index avg `0.0166` n `23`; metal avg `-0.0138` n `18`; unknown avg `-0.3698` n `365`
- 4h: commodity avg `-0.4206` n `12`; crypto_alt avg `0.0724` n `228`; crypto_major avg `-0.256` n `8`; equity avg `0.3778` n `65`; fx avg `0.1041` n `5`; index avg `0.2935` n `23`; metal avg `0.6342` n `18`; unknown avg `-0.2165` n `365`
- 24h: commodity avg `0.3743` n `12`; crypto_alt avg `2.2868` n `228`; crypto_major avg `-1.0462` n `8`; equity avg `-0.925` n `65`; fx avg `0.1557` n `5`; index avg `-0.6297` n `23`; metal avg `0.2055` n `18`; unknown avg `0.1438` n `355`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.132`, n `605`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1216`, n `605`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1125`, n `605`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1114`, n `605`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1096`, n `601`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1079`, n `601`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0907`, n `601`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0898`, n `601`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0792`, n `601`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.075`, n `605`, weak_sample_signal
