# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-10T10:52:30.151982+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.0108` n `12`; crypto_alt avg `-0.0192` n `233`; crypto_major avg `-0.0881` n `8`; equity avg `-0.0264` n `134`; fx avg `0.0097` n `6`; index avg `-0.0077` n `26`; metal avg `-0.0813` n `20`; unknown avg `0.3683` n `797`
- 1h: commodity avg `-0.0679` n `12`; crypto_alt avg `0.0292` n `233`; crypto_major avg `-0.0049` n `8`; equity avg `-0.0398` n `134`; fx avg `0.0237` n `6`; index avg `-0.003` n `26`; metal avg `-0.3801` n `20`; unknown avg `1.7749` n `795`
- 4h: commodity avg `0.1718` n `12`; crypto_alt avg `-1.0384` n `233`; crypto_major avg `-0.7433` n `8`; equity avg `-0.4484` n `134`; fx avg `0.0357` n `6`; index avg `-0.0911` n `26`; metal avg `-0.6291` n `20`; unknown avg `0.0607` n `789`
- 24h: commodity avg `-0.0402` n `12`; crypto_alt avg `-4.1054` n `233`; crypto_major avg `-2.7108` n `8`; equity avg `-0.7837` n `134`; fx avg `0.107` n `6`; index avg `-0.0047` n `26`; metal avg `-0.3008` n `20`; unknown avg `-0.6692` n `668`

## Correlations

- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `0.1311`, n `668`, weak_sample_signal
- market_context_score -> crypto_alt_forward_1h_return_pct: corr `0.1208`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1144`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.1052`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1`, n `668`, weak_sample_signal
- news_risk_score -> unknown_forward_1h_return_pct: corr `0.0996`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.094`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.0926`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `0.0907`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `0.0826`, n `668`, weak_sample_signal
