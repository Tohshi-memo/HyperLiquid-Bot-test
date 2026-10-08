# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-10-08T23:37:27.738784+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.002` n `13`; crypto_alt avg `-0.1011` n `235`; crypto_major avg `-0.0852` n `8`; equity avg `-0.1188` n `150`; fx avg `0.0087` n `6`; index avg `-0.0117` n `26`; metal avg `0.0087` n `20`; unknown avg `-0.1315` n `1077`
- 1h: commodity avg `0.0323` n `13`; crypto_alt avg `0.0863` n `235`; crypto_major avg `0.025` n `8`; equity avg `-0.2242` n `150`; fx avg `0.0154` n `6`; index avg `-0.0343` n `26`; metal avg `0.0458` n `20`; unknown avg `-0.2076` n `1075`
- 4h: commodity avg `-0.073` n `13`; crypto_alt avg `0.8625` n `235`; crypto_major avg `0.616` n `8`; equity avg `0.3615` n `150`; fx avg `0.0285` n `6`; index avg `0.0604` n `26`; metal avg `0.113` n `20`; unknown avg `-0.2553` n `1007`
- 24h: commodity avg `0.5309` n `13`; crypto_alt avg `-3.0667` n `235`; crypto_major avg `-3.4478` n `8`; equity avg `-2.9034` n `150`; fx avg `0.0655` n `6`; index avg `-0.3841` n `26`; metal avg `0.0558` n `20`; unknown avg `6.5053` n `991`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `0.1806`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1634`, n `668`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.1417`, n `668`, weak_sample_signal
- risk_on_score -> fx_forward_1h_return_pct: corr `0.1399`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.1319`, n `668`, weak_sample_signal
- market_context_score -> equity_forward_1h_return_pct: corr `-0.125`, n `668`, weak_sample_signal
- market_context_score -> fx_forward_1h_return_pct: corr `0.1246`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.1218`, n `668`, weak_sample_signal
- risk_on_score -> crypto_alt_forward_1h_return_pct: corr `-0.1202`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `-0.1126`, n `668`, weak_sample_signal
