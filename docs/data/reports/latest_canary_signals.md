# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-18T15:37:20.614467+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0521` n `12`; crypto_alt avg `-0.0415` n `228`; crypto_major avg `0.3148` n `8`; equity avg `0.2544` n `66`; fx avg `0.0122` n `5`; index avg `0.0375` n `23`; metal avg `0.1288` n `18`; unknown avg `0.1587` n `384`
- 1h: commodity avg `0.2984` n `12`; crypto_alt avg `-0.4162` n `228`; crypto_major avg `-0.3051` n `8`; equity avg `0.0206` n `66`; fx avg `-0.013` n `5`; index avg `-0.1131` n `23`; metal avg `0.1093` n `18`; unknown avg `-0.1756` n `384`
- 4h: commodity avg `0.2567` n `12`; crypto_alt avg `-0.3455` n `228`; crypto_major avg `-0.4485` n `8`; equity avg `-1.0452` n `66`; fx avg `-0.037` n `5`; index avg `-0.226` n `23`; metal avg `0.2231` n `18`; unknown avg `0.2617` n `383`
- 24h: commodity avg `0.8475` n `12`; crypto_alt avg `-3.0218` n `228`; crypto_major avg `-2.078` n `8`; equity avg `-0.6447` n `66`; fx avg `0.0624` n `5`; index avg `-0.3901` n `23`; metal avg `0.3986` n `18`; unknown avg `-0.3683` n `363`

## Correlations

- flow_alert_score -> index_forward_1h_return_pct: corr `-0.1573`, n `668`, weak_sample_signal
- polymarket_volume_24h -> index_forward_1h_return_pct: corr `-0.1526`, n `668`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1494`, n `668`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.1196`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1135`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1133`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1088`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `-0.1045`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `-0.1005`, n `668`, weak_sample_signal
