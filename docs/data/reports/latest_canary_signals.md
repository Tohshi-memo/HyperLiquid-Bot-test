# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-11-25T14:22:28.378767+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.1063` n `13`; crypto_alt avg `0.037` n `239`; crypto_major avg `0.2379` n `8`; equity avg `0.0327` n `168`; fx avg `-0.0041` n `6`; index avg `-0.0118` n `27`; metal avg `-0.0855` n `20`; unknown avg `0.0557` n `1261`
- 1h: commodity avg `0.0469` n `13`; crypto_alt avg `-0.7414` n `239`; crypto_major avg `-0.8527` n `8`; equity avg `-0.7127` n `168`; fx avg `0.02` n `6`; index avg `-0.0726` n `27`; metal avg `-0.3103` n `20`; unknown avg `-0.2836` n `1255`
- 4h: commodity avg `0.1776` n `13`; crypto_alt avg `-1.5195` n `239`; crypto_major avg `-1.0308` n `8`; equity avg `-1.054` n `168`; fx avg `0.0359` n `6`; index avg `-0.1317` n `27`; metal avg `-0.3988` n `20`; unknown avg `336.2063` n `1187`
- 24h: commodity avg `0.2526` n `13`; crypto_alt avg `-2.8176` n `239`; crypto_major avg `-3.7023` n `8`; equity avg `-5.566` n `168`; fx avg `-0.0447` n `6`; index avg `-0.4907` n `27`; metal avg `-1.3087` n `20`; unknown avg `631.7736` n `1065`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1433`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.1291`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `0.1241`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.112`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1107`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1106`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0931`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0917`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0846`, n `668`, weak_sample_signal
