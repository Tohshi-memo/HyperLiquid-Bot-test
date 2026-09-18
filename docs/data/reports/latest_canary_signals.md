# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-18T18:37:36.445139+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0114` n `12`; crypto_alt avg `-0.0077` n `234`; crypto_major avg `0.1851` n `8`; equity avg `-0.0634` n `140`; fx avg `-0.0054` n `6`; index avg `0.003` n `26`; metal avg `-0.0333` n `20`; unknown avg `7.797` n `940`
- 1h: commodity avg `0.0086` n `12`; crypto_alt avg `0.2738` n `234`; crypto_major avg `0.5772` n `8`; equity avg `0.0301` n `140`; fx avg `0.0073` n `6`; index avg `0.0291` n `26`; metal avg `-0.0194` n `20`; unknown avg `8.6109` n `938`
- 4h: commodity avg `-0.2228` n `12`; crypto_alt avg `0.813` n `234`; crypto_major avg `0.8876` n `8`; equity avg `0.3475` n `140`; fx avg `-0.0742` n `6`; index avg `0.0376` n `26`; metal avg `0.2122` n `20`; unknown avg `9.8097` n `908`
- 24h: commodity avg `-0.1708` n `12`; crypto_alt avg `6.21` n `234`; crypto_major avg `7.0167` n `8`; equity avg `0.7231` n `140`; fx avg `0.185` n `6`; index avg `-0.0767` n `26`; metal avg `0.3893` n `20`; unknown avg `9.3691` n `717`

## Correlations

- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.1461`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `-0.1418`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.1401`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1352`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1343`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.131`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.1244`, n `668`, weak_sample_signal
- market_context_score -> crypto_major_forward_1h_return_pct: corr `-0.1184`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.1171`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1132`, n `668`, weak_sample_signal
