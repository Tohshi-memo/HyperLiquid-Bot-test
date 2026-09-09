# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-09T10:52:28.998240+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0289` n `12`; crypto_alt avg `-0.1189` n `233`; crypto_major avg `-0.1696` n `8`; equity avg `-0.1547` n `134`; fx avg `0.0043` n `6`; index avg `-0.0402` n `26`; metal avg `-0.0144` n `20`; unknown avg `12.2863` n `798`
- 1h: commodity avg `-0.0289` n `12`; crypto_alt avg `-0.2508` n `233`; crypto_major avg `-0.0962` n `8`; equity avg `-0.2777` n `134`; fx avg `0.0115` n `6`; index avg `-0.0747` n `26`; metal avg `0.0294` n `20`; unknown avg `11.9205` n `796`
- 4h: commodity avg `0.1265` n `12`; crypto_alt avg `-0.5383` n `233`; crypto_major avg `-0.527` n `8`; equity avg `-0.7137` n `134`; fx avg `0.0076` n `6`; index avg `-0.1961` n `26`; metal avg `-0.0518` n `20`; unknown avg `0.9254` n `790`
- 24h: commodity avg `-0.0244` n `12`; crypto_alt avg `-0.5913` n `232`; crypto_major avg `0.4981` n `8`; equity avg `0.3173` n `134`; fx avg `-0.0782` n `6`; index avg `-0.1774` n `26`; metal avg `-0.0501` n `20`; unknown avg `1.1901` n `689`

## Correlations

- news_risk_score -> metal_forward_1h_return_pct: corr `0.1308`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1055`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1015`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.0947`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.0898`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0783`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `-0.0753`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0752`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0741`, n `668`, weak_sample_signal
