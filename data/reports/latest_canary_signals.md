# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-06-25T11:37:28.587512+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_index_leads_crypto: score `1.2871` - Index perps are stronger than crypto majors; possible risk-on canary.

## Class Returns

- 15m: commodity avg `0.0406` n `12`; crypto_alt avg `0.1243` n `228`; crypto_major avg `0.1209` n `8`; equity avg `-0.0236` n `86`; fx avg `-0.001` n `6`; index avg `-0.0432` n `23`; metal avg `-0.0527` n `20`; unknown avg `0.1059` n `765`
- 1h: commodity avg `0.0273` n `12`; crypto_alt avg `-0.2064` n `228`; crypto_major avg `-0.4376` n `8`; equity avg `-0.2196` n `86`; fx avg `-0.01` n `6`; index avg `-0.0413` n `23`; metal avg `-0.1185` n `20`; unknown avg `0.0361` n `765`
- 4h: commodity avg `0.0285` n `12`; crypto_alt avg `-0.7107` n `228`; crypto_major avg `-1.3182` n `8`; equity avg `-0.0793` n `86`; fx avg `-0.017` n `6`; index avg `-0.0311` n `23`; metal avg `0.1521` n `20`; unknown avg `0.0434` n `765`
- 24h: commodity avg `-0.2122` n `12`; crypto_alt avg `-1.3455` n `228`; crypto_major avg `-1.4669` n `8`; equity avg `0.0481` n `86`; fx avg `-0.0185` n `6`; index avg `0.4645` n `23`; metal avg `-0.969` n `20`; unknown avg `-0.6292` n `700`

## Correlations

- flow_alert_score -> unknown_forward_1h_return_pct: corr `0.1227`, n `668`, weak_sample_signal
- polymarket_volume_24h -> unknown_forward_1h_return_pct: corr `0.0894`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0889`, n `668`, weak_sample_signal
- polymarket_volume_24h -> metal_forward_1h_return_pct: corr `-0.0873`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `-0.0814`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.0733`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.0669`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.066`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.0645`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `-0.0592`, n `668`, weak_sample_signal
