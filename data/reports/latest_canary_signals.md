# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-09-06T16:07:30.140125+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0036` n `12`; crypto_alt avg `-0.0554` n `232`; crypto_major avg `-0.076` n `8`; equity avg `-0.0163` n `134`; fx avg `-0.0016` n `6`; index avg `0.0005` n `26`; metal avg `0.0043` n `20`; unknown avg `-0.3152` n `791`
- 1h: commodity avg `-0.0067` n `12`; crypto_alt avg `0.4686` n `232`; crypto_major avg `0.0561` n `8`; equity avg `0.0782` n `134`; fx avg `-0.0046` n `6`; index avg `0.0262` n `26`; metal avg `0.0034` n `20`; unknown avg `-0.2443` n `790`
- 4h: commodity avg `0.0619` n `12`; crypto_alt avg `-0.6822` n `232`; crypto_major avg `-0.6846` n `8`; equity avg `-0.2487` n `134`; fx avg `-0.0092` n `6`; index avg `-0.0357` n `26`; metal avg `-0.0152` n `20`; unknown avg `226.9599` n `720`
- 24h: commodity avg `0.0945` n `12`; crypto_alt avg `1.4234` n `232`; crypto_major avg `0.5456` n `8`; equity avg `0.2167` n `134`; fx avg `-0.0141` n `6`; index avg `0.0358` n `26`; metal avg `-0.0147` n `20`; unknown avg `1.61` n `664`

## Correlations

- news_risk_score -> unknown_forward_1h_return_pct: corr `-0.1464`, n `668`, weak_sample_signal
- news_risk_score -> crypto_major_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- flow_alert_score -> equity_forward_1h_return_pct: corr `0.1364`, n `668`, weak_sample_signal
- polymarket_volume_24h -> equity_forward_1h_return_pct: corr `0.1256`, n `668`, weak_sample_signal
- flow_alert_score -> metal_forward_1h_return_pct: corr `0.1158`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `0.1147`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `0.1118`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `0.1111`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `0.1109`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.1075`, n `668`, weak_sample_signal
