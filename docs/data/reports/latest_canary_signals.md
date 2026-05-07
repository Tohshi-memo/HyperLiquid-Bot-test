# Latest Canary Signals

These are early-warning indicators for cross-market relationships. They are hypotheses to test, not trade signals by themselves.

- Updated: `2026-05-07T17:07:19.168621+00:00`
- Correlation status: `ready`
- Asset price records: `568`
- Minimum samples for correlation: `24`

## Current Signals

- 4h_commodity_crypto_divergence: score `-3.2129` - Commodity perps and crypto are moving differently; check macro-linked stress.

## Class Returns

- 15m: commodity avg `-0.0982` n `12`; crypto_alt avg `0.034` n `228`; crypto_major avg `0.0336` n `8`; equity avg `0.0569` n `65`; fx avg `-0.0016` n `5`; index avg `0.044` n `23`; metal avg `0.1567` n `18`; unknown avg `0.0353` n `365`
- 1h: commodity avg `0.496` n `12`; crypto_alt avg `0.6766` n `228`; crypto_major avg `0.2291` n `8`; equity avg `0.0135` n `65`; fx avg `0.0164` n `5`; index avg `-0.1068` n `23`; metal avg `0.0442` n `18`; unknown avg `1.3192` n `365`
- 4h: commodity avg `1.8191` n `12`; crypto_alt avg `-1.0346` n `228`; crypto_major avg `-1.3938` n `8`; equity avg `-1.3396` n `65`; fx avg `0.0601` n `5`; index avg `-0.6863` n `23`; metal avg `-1.0452` n `18`; unknown avg `-0.5057` n `365`
- 24h: commodity avg `0.3908` n `12`; crypto_alt avg `0.1051` n `228`; crypto_major avg `-2.1382` n `8`; equity avg `-0.4035` n `65`; fx avg `0.1987` n `5`; index avg `-0.2852` n `23`; metal avg `0.944` n `18`; unknown avg `0.721` n `353`

## Correlations

- risk_on_score -> metal_forward_1h_return_pct: corr `-0.1343`, n `564`, weak_sample_signal
- polymarket_volume_24h -> crypto_major_forward_1h_return_pct: corr `-0.1155`, n `564`, weak_sample_signal
- market_context_score -> metal_forward_1h_return_pct: corr `-0.1151`, n `564`, weak_sample_signal
- flow_alert_score -> crypto_major_forward_1h_return_pct: corr `-0.1063`, n `564`, weak_sample_signal
- flow_alert_score -> fx_forward_1h_return_pct: corr `0.1006`, n `560`, weak_sample_signal
- polymarket_volume_24h -> fx_forward_1h_return_pct: corr `0.0951`, n `560`, weak_sample_signal
- risk_on_score -> commodity_forward_1h_return_pct: corr `0.0922`, n `560`, weak_sample_signal
- risk_on_score -> equity_forward_1h_return_pct: corr `-0.0891`, n `560`, weak_sample_signal
- news_risk_score -> index_forward_1h_return_pct: corr `-0.0831`, n `560`, weak_sample_signal
- news_risk_score -> crypto_alt_forward_1h_return_pct: corr `-0.0741`, n `564`, weak_sample_signal
