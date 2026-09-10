# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T06:06:06.515699+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0342` n `12`; crypto_alt avg `-0.1107` n `233`; crypto_major avg `-0.1034` n `8`; equity avg `0.0241` n `134`; fx avg `-0.0177` n `6`; index avg `0.0114` n `26`; metal avg `-0.0297` n `20`; unknown avg `0.0346` n `773`
- 1h: commodity avg `-0.1217` n `12`; crypto_alt avg `0.3605` n `233`; crypto_major avg `0.12` n `8`; equity avg `0.0988` n `134`; fx avg `0.0165` n `6`; index avg `0.0315` n `26`; metal avg `0.064` n `20`; unknown avg `0.1169` n `773`
- 4h: commodity avg `-0.1566` n `12`; crypto_alt avg `0.669` n `233`; crypto_major avg `0.3738` n `8`; equity avg `0.3881` n `134`; fx avg `0.0201` n `6`; index avg `0.1142` n `26`; metal avg `0.0461` n `20`; unknown avg `25.0442` n `767`
- 24h: commodity avg `-0.066` n `12`; crypto_alt avg `-3.2716` n `233`; crypto_major avg `-2.2354` n `8`; equity avg `-0.9562` n `134`; fx avg `0.0695` n `6`; index avg `-0.1155` n `26`; metal avg `0.324` n `20`; unknown avg `0.2961` n `670`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1224`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1085`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1067`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.1032`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `0.1011`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0963`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0823`, n `668`, weak_sample_signal
- market_context_score -> unknown_forward_1h_return_pct: corr `-0.082`, n `668`, weak_sample_signal
