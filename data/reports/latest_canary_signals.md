# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T09:22:25.595751+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.1069` n `12`; crypto_alt avg `0.061` n `230`; crypto_major avg `0.1492` n `8`; equity avg `-0.0166` n `102`; fx avg `0.0255` n `6`; index avg `-0.0139` n `25`; metal avg `0.0003` n `20`; unknown avg `0.1123` n `782`
- 1h: commodity avg `-0.0852` n `12`; crypto_alt avg `-0.0553` n `230`; crypto_major avg `-0.1827` n `8`; equity avg `-0.207` n `102`; fx avg `0.0107` n `6`; index avg `-0.0383` n `25`; metal avg `-0.0162` n `20`; unknown avg `0.0651` n `782`
- 4h: commodity avg `-0.1884` n `12`; crypto_alt avg `-0.0181` n `230`; crypto_major avg `-0.3417` n `8`; equity avg `0.0334` n `102`; fx avg `-0.0212` n `6`; index avg `0.0068` n `25`; metal avg `0.0023` n `20`; unknown avg `-0.0111` n `766`
- 24h: commodity avg `-1.245` n `12`; crypto_alt avg `0.3418` n `230`; crypto_major avg `0.2615` n `8`; equity avg `0.8547` n `102`; fx avg `-0.1594` n `6`; index avg `0.2594` n `25`; metal avg `0.239` n `20`; unknown avg `0.2691` n `765`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1312`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1209`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1113`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.093`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0881`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0786`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.072`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0719`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0694`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0684`, n `668`, weak_sample_signal
