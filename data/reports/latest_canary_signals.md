# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-05T20:22:50.620533+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0179` n `12`; crypto_alt avg `0.1366` n `230`; crypto_major avg `0.061` n `8`; equity avg `0.1038` n `108`; fx avg `-0.0071` n `6`; index avg `0.0265` n `25`; metal avg `-0.0122` n `20`; unknown avg `0.0391` n `782`
- 1h: commodity avg `-0.0475` n `12`; crypto_alt avg `-0.0132` n `230`; crypto_major avg `-0.1072` n `8`; equity avg `-0.9445` n `108`; fx avg `0.0162` n `6`; index avg `-0.1042` n `25`; metal avg `-0.0717` n `20`; unknown avg `0.0554` n `782`
- 4h: commodity avg `-0.155` n `12`; crypto_alt avg `0.1012` n `230`; crypto_major avg `0.1255` n `8`; equity avg `-1.0628` n `108`; fx avg `-0.0061` n `6`; index avg `-0.1015` n `25`; metal avg `0.0707` n `20`; unknown avg `-0.1012` n `782`
- 24h: commodity avg `-0.0079` n `12`; crypto_alt avg `0.7582` n `230`; crypto_major avg `0.9952` n `8`; equity avg `-0.483` n `108`; fx avg `-0.0422` n `6`; index avg `-0.1031` n `25`; metal avg `0.7982` n `20`; unknown avg `0.8444` n `749`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1451`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.1342`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.1024`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1006`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.097`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0898`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `0.0711`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0694`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0672`, n `668`, weak_sample_signal
