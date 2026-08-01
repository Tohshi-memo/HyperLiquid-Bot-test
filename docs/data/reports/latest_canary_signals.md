# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T08:52:28.626183+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0199` n `12`; crypto_alt avg `0.0339` n `230`; crypto_major avg `0.0335` n `8`; equity avg `-0.0254` n `102`; fx avg `-0.0098` n `6`; index avg `-0.006` n `25`; metal avg `-0.0009` n `20`; unknown avg `-0.0048` n `781`
- 1h: commodity avg `0.0499` n `12`; crypto_alt avg `0.1253` n `230`; crypto_major avg `0.0484` n `8`; equity avg `0.006` n `102`; fx avg `-0.0153` n `6`; index avg `-0.0166` n `25`; metal avg `-0.0048` n `20`; unknown avg `-0.1276` n `781`
- 4h: commodity avg `0.0025` n `12`; crypto_alt avg `-0.182` n `230`; crypto_major avg `-0.2207` n `8`; equity avg `0.0445` n `102`; fx avg `0.0079` n `6`; index avg `-0.0217` n `25`; metal avg `0.0439` n `20`; unknown avg `-0.0047` n `765`
- 24h: commodity avg `0.8812` n `12`; crypto_alt avg `0.1926` n `230`; crypto_major avg `-1.2705` n `8`; equity avg `-2.627` n `102`; fx avg `-0.0137` n `6`; index avg `-0.2926` n `25`; metal avg `-0.0787` n `20`; unknown avg `4.8406` n `764`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1079`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1072`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1036`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.08`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.074`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0705`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.0648`, n `668`, weak_sample_signal
