# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T02:37:30.273249+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0039` n `12`; crypto_alt avg `-0.1219` n `230`; crypto_major avg `-0.1009` n `8`; equity avg `-0.1713` n `102`; fx avg `0.0112` n `6`; index avg `-0.0057` n `25`; metal avg `0.0216` n `20`; unknown avg `-0.0042` n `782`
- 1h: commodity avg `-0.5929` n `12`; crypto_alt avg `0.3685` n `230`; crypto_major avg `0.4755` n `8`; equity avg `0.6511` n `102`; fx avg `-0.0001` n `6`; index avg `0.1195` n `25`; metal avg `0.0625` n `20`; unknown avg `1.1681` n `782`
- 4h: commodity avg `-0.8977` n `12`; crypto_alt avg `0.8857` n `230`; crypto_major avg `0.9585` n `8`; equity avg `0.9568` n `102`; fx avg `-0.0246` n `6`; index avg `0.2088` n `25`; metal avg `0.0843` n `20`; unknown avg `1.3237` n `782`
- 24h: commodity avg `-0.9214` n `12`; crypto_alt avg `-0.0284` n `230`; crypto_major avg `-0.054` n `8`; equity avg `0.7273` n `102`; fx avg `-0.0354` n `6`; index avg `0.1492` n `25`; metal avg `0.1594` n `20`; unknown avg `-0.0839` n `765`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1176`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1131`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1122`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0974`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0904`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0782`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0708`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0695`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0685`, n `668`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `0.068`, n `668`, weak_sample_signal
