# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-02T18:52:31.556776+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0155` n `12`; crypto_alt avg `-0.0118` n `230`; crypto_major avg `-0.0291` n `8`; equity avg `0.0068` n `102`; fx avg `-0.0056` n `6`; index avg `0.0087` n `25`; metal avg `-0.0033` n `20`; unknown avg `0.0759` n `782`
- 1h: commodity avg `-0.0071` n `12`; crypto_alt avg `0.1426` n `230`; crypto_major avg `0.2912` n `8`; equity avg `0.0947` n `102`; fx avg `0.008` n `6`; index avg `0.009` n `25`; metal avg `0.028` n `20`; unknown avg `0.1319` n `782`
- 4h: commodity avg `-0.1167` n `12`; crypto_alt avg `0.2146` n `230`; crypto_major avg `0.7521` n `8`; equity avg `0.4137` n `102`; fx avg `0.0132` n `6`; index avg `0.0481` n `25`; metal avg `0.0801` n `20`; unknown avg `1.5832` n `782`
- 24h: commodity avg `-1.2699` n `12`; crypto_alt avg `1.9274` n `230`; crypto_major avg `2.4382` n `8`; equity avg `1.6092` n `102`; fx avg `-0.1298` n `6`; index avg `0.3218` n `25`; metal avg `0.3548` n `20`; unknown avg `1.6935` n `766`

## Correlations

- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.1344`, n `668`, weak_sample_signal
- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1205`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.1194`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0869`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0844`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0793`, n `668`, weak_sample_signal
- risk_on_score -> unknown_forward_1h_return_pct: corr `0.0722`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0701`, n `668`, weak_sample_signal
- news_risk_score -> fx_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
