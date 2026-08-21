# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-21T05:07:25.664282+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0458` n `12`; crypto_alt avg `-0.1051` n `230`; crypto_major avg `-0.049` n `8`; equity avg `0.0745` n `121`; fx avg `0.0022` n `6`; index avg `-0.0008` n `25`; metal avg `-0.0339` n `20`; unknown avg `0.2619` n `793`
- 1h: commodity avg `-0.0555` n `12`; crypto_alt avg `0.2376` n `230`; crypto_major avg `0.1874` n `8`; equity avg `0.11` n `121`; fx avg `-0.0089` n `6`; index avg `0.0108` n `25`; metal avg `-0.0055` n `20`; unknown avg `0.1212` n `793`
- 4h: commodity avg `-0.0799` n `12`; crypto_alt avg `1.0246` n `230`; crypto_major avg `0.8264` n `8`; equity avg `0.5712` n `121`; fx avg `-0.0653` n `6`; index avg `0.1307` n `25`; metal avg `0.1861` n `20`; unknown avg `-0.0438` n `793`
- 24h: commodity avg `0.2348` n `12`; crypto_alt avg `5.7294` n `230`; crypto_major avg `6.8117` n `8`; equity avg `-0.4457` n `121`; fx avg `-0.0352` n `6`; index avg `-0.0645` n `25`; metal avg `0.4852` n `20`; unknown avg `2.6503` n `776`

## Correlations

- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.2119`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1877`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1858`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1811`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1243`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `-0.1125`, n `668`, weak_sample_signal
- flow_alert_score -> unknown_forward_1h_return_pct: corr `-0.1059`, n `668`, weak_sample_signal
- flow_alert_score -> index_forward_1h_return_pct: corr `-0.0998`, n `668`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `0.0938`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `0.0912`, n `668`, weak_sample_signal
