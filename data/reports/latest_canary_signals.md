# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-07-01T04:37:30.515855+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- polymarket_volume_spike: score `2.13` - Polymarket crypto volume is unusually high.
- 4h_crypto_metal_divergence: score `1.5129` - Crypto majors and metals are diverging; useful for risk/hedge regime checks.

## Class Returns

- 15m: commodity avg `-0.0017` n `12`; crypto_alt avg `-0.0988` n `228`; crypto_major avg `-0.0754` n `8`; equity avg `0.0212` n `88`; fx avg `-0.0168` n `6`; index avg `0.0075` n `23`; metal avg `-0.0058` n `20`; unknown avg `-0.3209` n `765`
- 1h: commodity avg `-0.0059` n `12`; crypto_alt avg `0.4054` n `228`; crypto_major avg `0.0441` n `8`; equity avg `0.0125` n `88`; fx avg `-0.0287` n `6`; index avg `0.0034` n `23`; metal avg `-0.0739` n `20`; unknown avg `0.2049` n `763`
- 4h: commodity avg `-0.0478` n `12`; crypto_alt avg `1.3225` n `228`; crypto_major avg `1.1559` n `8`; equity avg `-0.2974` n `88`; fx avg `0.0132` n `6`; index avg `-0.1638` n `23`; metal avg `-0.357` n `20`; unknown avg `1.3543` n `763`
- 24h: commodity avg `0.1126` n `12`; crypto_alt avg `-0.2258` n `228`; crypto_major avg `-0.0666` n `8`; equity avg `0.361` n `88`; fx avg `0.1603` n `6`; index avg `-0.0873` n `23`; metal avg `-0.4001` n `20`; unknown avg `-0.8852` n `733`

## Correlations

- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- news_risk_score -> metal_forward_1h_return_pct: corr `-0.1165`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1063`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.0892`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.089`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.0795`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `0.0776`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `-0.0725`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.0715`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.0682`, n `668`, weak_sample_signal
