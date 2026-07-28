# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-28T11:37:27.917025+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0895` n `12`; crypto_alt avg `-0.0855` n `230`; crypto_major avg `-0.0415` n `8`; equity avg `-0.1475` n `102`; fx avg `0.0054` n `6`; index avg `-0.0285` n `25`; metal avg `0.0008` n `20`; unknown avg `-0.059` n `774`
- 1h: commodity avg `0.0235` n `12`; crypto_alt avg `-0.1212` n `230`; crypto_major avg `-0.1598` n `8`; equity avg `-0.3595` n `102`; fx avg `0.0107` n `6`; index avg `-0.0069` n `25`; metal avg `0.0474` n `20`; unknown avg `-0.113` n `774`
- 4h: commodity avg `-0.0344` n `12`; crypto_alt avg `-0.2078` n `230`; crypto_major avg `-0.2784` n `8`; equity avg `-0.6747` n `102`; fx avg `-0.0296` n `6`; index avg `-0.1151` n `25`; metal avg `-0.2003` n `20`; unknown avg `-0.1396` n `774`
- 24h: commodity avg `-0.4439` n `12`; crypto_alt avg `-3.7293` n `230`; crypto_major avg `-3.7995` n `8`; equity avg `-4.4843` n `102`; fx avg `-0.1771` n `6`; index avg `-0.9199` n `25`; metal avg `-0.6459` n `20`; unknown avg `1225.2382` n `758`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1594`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1301`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.1121`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1089`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1006`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0987`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `-0.0937`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.0822`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.0792`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0751`, n `668`, weak_sample_signal
