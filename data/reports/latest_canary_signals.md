# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T18:37:23.740225+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `0.053` n `12`; crypto_alt avg `0.0945` n `230`; crypto_major avg `0.2138` n `8`; equity avg `0.042` n `102`; fx avg `0.0101` n `6`; index avg `-0.0006` n `25`; metal avg `0.0057` n `20`; unknown avg `0.0606` n `782`
- 1h: commodity avg `0.0282` n `12`; crypto_alt avg `0.1591` n `230`; crypto_major avg `0.3386` n `8`; equity avg `0.0884` n `102`; fx avg `0.0247` n `6`; index avg `-0.0081` n `25`; metal avg `0.0389` n `20`; unknown avg `0.0451` n `782`
- 4h: commodity avg `-0.0876` n `12`; crypto_alt avg `0.1914` n `230`; crypto_major avg `0.7777` n `8`; equity avg `0.3886` n `102`; fx avg `0.0224` n `6`; index avg `0.0432` n `25`; metal avg `0.096` n `20`; unknown avg `1.3404` n `782`
- 24h: commodity avg `-1.2378` n `12`; crypto_alt avg `1.582` n `230`; crypto_major avg `2.0148` n `8`; equity avg `1.5637` n `102`; fx avg `-0.1137` n `6`; index avg `0.309` n `25`; metal avg `0.3544` n `20`; unknown avg `1.6182` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1332`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1196`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1183`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0866`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0858`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0788`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0723`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0703`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0675`, n `668`, weak_sample_signal
