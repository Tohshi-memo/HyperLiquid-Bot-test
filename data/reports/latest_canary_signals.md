# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T02:52:11.609948+00:00`
- Correlation status: `ready`
- Asset price records: `511`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.56` - Polymarket crypto volume is unusually high.

## Class Returns

- 15m: commodity avg `-0.0184` n `12`; crypto_alt avg `0.1406` n `228`; crypto_major avg `0.0534` n `8`; equity avg `-0.0388` n `65`; fx avg `0.0215` n `4`; index avg `0.0484` n `23`; metal avg `0.0616` n `18`; unknown avg `-0.0392` n `358`
- 1h: commodity avg `-0.0267` n `12`; crypto_alt avg `-0.0672` n `228`; crypto_major avg `-0.194` n `8`; equity avg `-0.0553` n `65`; fx avg `0.0383` n `4`; index avg `0.0033` n `23`; metal avg `-0.3562` n `18`; unknown avg `-0.4577` n `358`
- 4h: commodity avg `-0.2011` n `12`; crypto_alt avg `-0.8427` n `228`; crypto_major avg `-0.793` n `8`; equity avg `0.0059` n `65`; fx avg `0.0894` n `4`; index avg `0.1802` n `23`; metal avg `0.2274` n `18`; unknown avg `-0.451` n `356`
- 24h: commodity avg `-1.8217` n `7`; crypto_alt avg `0.4823` n `223`; crypto_major avg `-0.7427` n `7`; equity avg `1.6325` n `47`; fx avg `-0.2727` n `4`; index avg `1.3348` n `6`; metal avg `2.0692` n `7`; unknown avg `2.2591` n `311`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1327`, n `507`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1182`, n `507`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0953`, n `507`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.0815`, n `507`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0759`, n `503`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0697`, n `503`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0694`, n `503`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0692`, n `503`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0685`, n `507`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0647`, n `503`, weak_sample_signal
