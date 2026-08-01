# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-08-01T15:37:33.389885+00:00`
- Correlation status: `ready`
- Asset price records: `672`
- Minimum samples for correlation: `24`

## Current Signals

- baseline: score `0` - No elevated canary signal. Continue collecting samples.

## Class Returns

- 15m: commodity avg `-0.0017` n `12`; crypto_alt avg `-0.0202` n `230`; crypto_major avg `-0.08` n `8`; equity avg `-0.0268` n `102`; fx avg `-0.0055` n `6`; index avg `0.0109` n `25`; metal avg `-0.0038` n `20`; unknown avg `0.0153` n `782`
- 1h: commodity avg `0.0072` n `12`; crypto_alt avg `-0.1379` n `230`; crypto_major avg `-0.0933` n `8`; equity avg `-0.034` n `102`; fx avg `0.0043` n `6`; index avg `-0.01` n `25`; metal avg `0.0229` n `20`; unknown avg `-0.0132` n `782`
- 4h: commodity avg `-0.0139` n `12`; crypto_alt avg `0.015` n `230`; crypto_major avg `0.0666` n `8`; equity avg `-0.1971` n `102`; fx avg `0.078` n `6`; index avg `0.009` n `25`; metal avg `0.0205` n `20`; unknown avg `-0.1142` n `781`
- 24h: commodity avg `0.5255` n `12`; crypto_alt avg `0.2818` n `230`; crypto_major avg `-0.4349` n `8`; equity avg `-0.2914` n `102`; fx avg `-0.0655` n `6`; index avg `0.046` n `25`; metal avg `0.0402` n `20`; unknown avg `4.0801` n `764`

## Correlations

- news_risk_score -> commodity_forward_1h_return_pct: corr `-0.1171`, n `668`, weak_sample_signal
- risk_on_score -> crypto_major_forward_1h_return_pct: corr `-0.0977`, n `668`, weak_sample_signal
- polymarket_volume_24h -> crypto_alt_forward_1h_return_pct: corr `-0.0976`, n `668`, weak_sample_signal
- flow_alert_score -> commodity_forward_1h_return_pct: corr `0.0901`, n `668`, weak_sample_signal
- polymarket_volume_24h -> commodity_forward_1h_return_pct: corr `0.0893`, n `668`, weak_sample_signal
- market_context_score -> commodity_forward_1h_return_pct: corr `0.0808`, n `668`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `0.0704`, n `668`, weak_sample_signal
- flow_alert_score -> crypto_alt_forward_1h_return_pct: corr `-0.069`, n `668`, weak_sample_signal
- risk_on_score -> metal_forward_1h_return_pct: corr `0.0663`, n `668`, weak_sample_signal
- news_risk_score -> equity_forward_1h_return_pct: corr `0.0656`, n `668`, weak_sample_signal
