# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-21T05:52:27.960324+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0609` n `13`; crypto_alt avg `-0.1667` n `237`; crypto_major avg `-0.2431` n `8`; equity avg `-0.0408` n `151`; fx avg `0.0014` n `6`; index avg `-0.0111` n `26`; metal avg `-0.0481` n `20`; unknown avg `96.9381` n `1200`
- 1h: commodity avg `0.0884` n `13`; crypto_alt avg `-0.1386` n `237`; crypto_major avg `-0.0365` n `8`; equity avg `-0.0328` n `151`; fx avg `0.0125` n `6`; index avg `-0.0136` n `26`; metal avg `0.0085` n `20`; unknown avg `2.7546` n `1198`
- 4h: commodity avg `0.0478` n `13`; crypto_alt avg `-0.7497` n `237`; crypto_major avg `-0.7524` n `8`; equity avg `-0.5296` n `151`; fx avg `-0.0455` n `6`; index avg `-0.1211` n `26`; metal avg `-0.1063` n `20`; unknown avg `2.5555` n `1191`
- 24h: commodity avg `0.0541` n `13`; crypto_alt avg `2.2154` n `237`; crypto_major avg `1.544` n `8`; equity avg `2.5489` n `151`; fx avg `0.0153` n `6`; index avg `0.3247` n `26`; metal avg `-0.0784` n `20`; unknown avg `221.0819` n `990`

## Correlations

- news_risk_score -> index_forward_1h_return_pct: corr `-0.1641`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1213`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `-0.1208`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1009`, n `668`, weak_sample_signal
- risk_on_score -> index_forward_1h_return_pct: corr `-0.0958`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0947`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `-0.0879`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.0807`, n `668`, weak_sample_signal
